# https://stepik.org/lesson/237257/step/7?unit=209645

import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("Начало фикстуры prepare_faces")
    print("^_^")
    yield
    print("Конец фикстуры prepare_faces")
    print(":3")


@pytest.fixture()
def very_important_fixture():
    print("Фикстура very_important_fixture")
    print(":)")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("Фикстура print_smiling_faces")
    print(":-Р")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        assert 2 + 3 == 5

    def test_second_smiling_faces(self):
        assert 2 + 4 == 6
