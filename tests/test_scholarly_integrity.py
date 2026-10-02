import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ScholarlyIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.status = json.loads((ROOT / "analysis/current-status.json").read_text())
        cls.coverage = json.loads((ROOT / "research/coverage-register.json").read_text())
        cls.records = json.loads((ROOT / "data/records.json").read_text())
        cls.queue = json.loads((ROOT / "research/expert-review-queue.json").read_text())

    def test_status_counts_match_corpus(self):
        self.assertEqual(len(self.records), self.status["records"])
        self.assertEqual(len(self.coverage), self.status["coverage_register"]["entries"])

    def test_no_analysis_admission_before_review(self):
        eligible = [line for record in self.records for line in record.get("lines", []) if line.get("analysis_eligible")]
        self.assertEqual(eligible, [])
        self.assertFalse(self.status["independent_human_epigraphic_review"])

    def test_coverage_register_is_explicitly_incomplete(self):
        self.assertTrue(self.status["coverage_register"]["known_incomplete"])
        self.assertIn("exhaustive_world_corpus", self.status["blocked_claims"])

    def test_disputed_and_collection_objects_not_admitted(self):
        guarded = {"disputed_authenticity", "disputed_script", "collection_lead", "uncertain_language", "secondary_reference_only"}
        for item in self.coverage:
            if item["status"] in guarded:
                self.assertFalse(item["analysis_eligible"], item["object_id"])

    def test_expert_queue_objects_do_not_create_admission(self):
        self.assertTrue(self.queue["items"])
        self.assertIn("No item may become analysis_eligible", self.queue["admission_rule"])

if __name__ == "__main__":
    unittest.main()
