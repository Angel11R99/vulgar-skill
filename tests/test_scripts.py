import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_commit
import validate_catalog
import validate_commit


class SkillScriptsTests(unittest.TestCase):
    def test_catalogs_are_valid_and_populated(self):
        errors, files, total = validate_catalog.validate(ROOT / "catalogs")
        self.assertEqual(errors, [])
        self.assertEqual(len(files), 10)
        self.assertGreaterEqual(total, 100)

    def test_generator_respects_region_and_intensity(self):
        import random
        result = generate_commit.generate("fix token refresh behavior", "es", "mexican", "high", rng=random.Random(4), commit_type="fix", scope="auth")
        self.assertTrue(result.startswith("fix(auth): fix token refresh behavior"))
        self.assertTrue(any(term in result for term in ("chingados", "chingadera", "madres", "pinche", "carajo")))

    def test_validator_accepts_valid_header_and_terms(self):
        errors = validate_commit.validate("fix(auth): stop the damn shit refresh loop", ROOT / "catalogs", "high")
        self.assertEqual(errors, [])

    def test_validator_rejects_missing_terms(self):
        errors = validate_commit.validate("fix(auth): stop the refresh loop", ROOT / "catalogs", "high")
        self.assertTrue(any("requires at least" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
