from exif_utils import utils
import os


class TestUtils:
    def test_move_to_lower(self):
        tests = ["a.JPG", "b.PnG", "c.JPEg"]
        expected = ["a.jpg", "b.png", "c.jpeg"]
        utils._exec("touch {}".format(' '.join(tests)))
        utils.move_to_lower(tests)
        for filename in expected:
            assert os.path.exists(filename)
        utils._exec("rm {}".format(' '.join(expected)))

    def test_get_image_filepaths(self):
        tests = ["a.JPG", "b.PnG", "c.JPEg"]
        basedir = os.path.abspath('.')
        expected = [
            os.path.join(basedir, "a.JPG"),
            os.path.join(basedir, "b.PnG"),
            os.path.join(basedir, "c.JPEg")]
        utils._exec("touch {}".format(' '.join(tests)))
        actual = utils.get_image_filepaths(".")
        actual.sort()
        expected.sort()
        assert expected == actual
        utils._exec("rm {}".format(' '.join(tests)))


if __name__ == '__main__':
    TestUtils().test_move_to_lower()
    TestUtils().test_get_image_filepaths()
