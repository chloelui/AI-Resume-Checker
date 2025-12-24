import argparse
from src.io_utils import read_text
from src.preprocess import normalize
from src.matchers import tfidf_match_score, sim_to_score
from src.skills import missing_skills

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resume", required=True)
    ap.add_argument("--job", required=True)
    args = ap.parse_args()

    resume = normalize(read_text(args.resume))
    job = normalize(read_text(args.job))

    sim = tfidf_match_score(resume, job)
    score = sim_to_score(sim)

    miss, matched = missing_skills(resume, job)

    print(f"Match Score: {score}/100")
    print(f"Matched Skills ({len(matched)}): {matched}")
    print(f"Missing Skills ({len(miss)}): {miss}")

if __name__ == "__main__":
    main()