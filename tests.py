import subprocess


def test_app():
    # Arrange
    novels = ["The Door to Rebirth in Apocalypse",
              "Dying in the Male Lead’s Arms Every Time I Transmigrate",
              "I Married a Disabled Tyrant After Transmigrating"]
    input_data = "\n".join(novels) + "\n"

    # Act
    result = subprocess.run(["python", "main.py"],
                            input=input_data.encode(),
                            capture_output=True)

    # Assert
    assert result.returncode == 0
    assert b"Novels:" in result.stdout
    assert b"Task 0 with Novel 1 is created" in result.stdout
    assert b"Task 1 with Novel 2 is created" in result.stdout
    assert b"Task 2 with Novel 3 is created" in result.stdout
