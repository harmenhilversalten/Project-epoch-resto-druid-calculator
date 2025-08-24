import pathlib
import re
import unittest

class StyleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = pathlib.Path('index.html').read_text()

    def test_body_font(self):
        self.assertRegex(self.content, r"font-family:\s*'DM Sans'")

    def test_banner_image_present(self):
        self.assertIn('druid-bg.webp', self.content)

    def test_cta_color(self):
        self.assertIn('#16ba17', self.content)

if __name__ == '__main__':
    unittest.main()
