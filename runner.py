"""
나루 크롤러 실행 엔트리포인트

사용법:
  python runner.py --company hitachi --limit 10 --dry-run   # 미리보기 (적재 안 함)
  python runner.py --company hitachi --limit 50             # 실제 적재
  python runner.py --company hitachi --report-only          # 현재 DRAFT 리포트만
"""
import argparse
import sys
from datetime import datetime
from typing import List

from api.naru_client import NaruClient
from models.job import NaruJob
from validators.job_validator import validate

# 기업 크롤러 등록 (새 기업 추가 시 여기에 추가)
CRAWLERS = {
    "hitachi": lambda: __import__("companies.hitachi", fromlist=["HitachiCrawler"]).HitachiCrawler(),
}


def run_crawl(company: str, limit: int = None, dry_run: bool = False):
    """크롤링 실행"""
    if company not in CRAWLERS:
        print(f"❌ 등록되지 않은 기업: '{company}'")
        print(f"   등록된 기업: {list(CRAWLERS.keys())}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"🍇 나루 크롤러 시작: {company}")
    print(f"   모드: {'DRY RUN (적재 안 함)' if dry_run else '실제 적재'}")
    if limit:
        print(f"   제한: 최대 {limit}개")
    print(f"   시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    # 크롤링
    crawler = CRAWLERS[company]()
    jobs = crawler.crawl(limit=limit)

    # 품질 검증
    print(f"\n📋 품질 검증 중...")
    passed: List[NaruJob] = []
    failed = []

    for job in jobs:
        ok, reasons = validate(job)
        if ok:
            passed.append(job)
        else:
            failed.append({"title": job.title[:50], "reasons": reasons})
            print(f"  ❌ [{job.source_id}] {job.title[:40]}")
            for r in reasons:
                print(f"      → {r}")

    print(f"\n  통과: {len(passed)}개 / 실패: {len(failed)}개")

    # 적재
    created = []
    errors = []

    if not dry_run and passed:
        print(f"\n🚀 나루 API에 DRAFT 적재 중...")
        client = NaruClient()

        for i, job in enumerate(passed):
            try:
                result = client.create_job(job)
                job_id = result.get("jobId") or result.get("id", "?")
                created.append({"id": job_id, "title": job.title[:50], "source_id": job.source_id})
                print(f"  [{i+1}/{len(passed)}] ✅ ID={job_id} {job.title[:40]}")
            except Exception as e:
                errors.append({"title": job.title[:50], "error": str(e)})
                print(f"  [{i+1}/{len(passed)}] ❌ {job.title[:40]} → {e}")

    elif dry_run:
        print(f"\n📝 DRY RUN 결과 (실제 적재 안 됨):")
        for job in passed[:10]:
            print(f"  • [{job.position:10s}] [{job.experience_level:10s}] {job.title[:50]}")
            print(f"    위치: {job.locations} | 기술: {job.tech_stack[:3]}")
        if len(passed) > 10:
            print(f"  ... 외 {len(passed)-10}개")

    # 최종 리포트
    print(f"\n{'='*60}")
    print(f"📊 실행 결과 리포트")
    print(f"{'='*60}")
    print(f"기업:        {company}")
    print(f"전체 공고:   {len(jobs)}개")
    print(f"품질 통과:   {len(passed)}개")
    print(f"품질 실패:   {len(failed)}개")
    if not dry_run:
        print(f"적재 완료:   {len(created)}개")
        print(f"적재 실패:   {len(errors)}개")
    print(f"실행 시각:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if failed:
        print(f"\n❌ 품질 실패 목록:")
        for f in failed[:5]:
            print(f"  • {f['title']}")
            for r in f["reasons"]:
                print(f"    → {r}")
        if len(failed) > 5:
            print(f"  ... 외 {len(failed)-5}개")

    if errors:
        print(f"\n❌ 적재 실패 목록:")
        for e in errors:
            print(f"  • {e['title']}: {e['error']}")

    print(f"{'='*60}\n")
    return created, failed, errors


def report_only(company: str):
    """현재 DRAFT 공고 현황만 출력"""
    client = NaruClient()
    drafts = client.get_drafts()
    print(f"\n📋 현재 DRAFT 공고: {len(drafts)}개")
    for d in drafts:
        print(f"  ID={d.get('jobId')} | {d.get('title', '')[:50]} | {d.get('status')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="나루 채용 플랫폼 크롤러")
    parser.add_argument("--company", required=True, help=f"기업 slug ({', '.join(CRAWLERS.keys())})")
    parser.add_argument("--limit", type=int, default=None, help="최대 크롤링 수 (기본: 전체)")
    parser.add_argument("--dry-run", action="store_true", help="미리보기 (실제 적재 안 함)")
    parser.add_argument("--report-only", action="store_true", help="현재 DRAFT 리포트만 출력")

    args = parser.parse_args()

    if args.report_only:
        report_only(args.company)
    else:
        run_crawl(args.company, limit=args.limit, dry_run=args.dry_run)
