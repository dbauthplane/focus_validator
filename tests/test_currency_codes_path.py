import os
import tempfile
import unittest

from focus_validator.utils.download_currency_codes import (
    DEFAULT_CURRENCY_CODES_FILE,
    get_currency_codes,
)


class TestCurrencyCodesPath(unittest.TestCase):
    """The bundled currency list loads from any working directory."""

    def test_default_file_is_inside_package(self):
        self.assertTrue(DEFAULT_CURRENCY_CODES_FILE.is_file())

    def test_loads_outside_repo_root(self):
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            try:
                codes = get_currency_codes()
            finally:
                os.chdir(cwd)
        self.assertIn("USD", codes)
        self.assertIn("EUR", codes)


if __name__ == "__main__":
    unittest.main()
