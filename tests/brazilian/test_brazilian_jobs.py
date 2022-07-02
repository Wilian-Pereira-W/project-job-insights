from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dados = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert (
        dados[0].keys()
        == (
            {
                "salary": "",
                "title": "",
                "type": "",
            }
        ).keys()
    )
