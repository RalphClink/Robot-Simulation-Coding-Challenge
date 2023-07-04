# Test Isolation Principle,
# All tests should be able to run independent of one another

from controller import Controller


# Test Sample Input Scenario 1
def test_sample_input_1(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,0,NORTH")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "MOVE")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "0,1,NORTH"


# Test Sample Input Scenario 2
def test_sample_input_2(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,0,NORTH")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "LEFT")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "0,0,WEST"


# Test Invalid Coordinated are Ignored
def test_invalid_placement(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 6,6,NORTH")      # Place the robot out of bounds
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()
    print(controller.robot.report_position())

    assert controller.robot.report_position() == "Robot Not Yet Placed"     # Robot should not have been placed


# Test Out-of-Bounds North Move is Ignored
def test_out_of_bounds_north(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,4,NORTH")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "MOVE")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "0,4,NORTH"                # Move should have been ignored


# Test Out-of-Bounds South Move is Ignored
def test_out_of_bounds_south(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,0,SOUTH")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "MOVE")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "0,0,SOUTH"                # Move should have been ignored


# Test Out-of-Bounds East Move is Ignored
def test_out_of_bounds_east(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 4,0,EAST")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "MOVE")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "4,0,EAST"             # Move should have been ignored


# Test Out-of-Bounds West Move is Ignored
def test_out_of_bounds_west(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,0,WEST")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "MOVE")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "0,0,WEST"             # Move should have been ignored


# Test Robot Is Not Deployed with an Invalid Direction
def test_invalid_direction(monkeypatch):
    controller = Controller()
    monkeypatch.setattr('builtins.input', lambda _: "PLACE 0,0,BAD DIRECTION")
    controller.process_user_command()
    monkeypatch.setattr('builtins.input', lambda _: "REPORT")
    controller.process_user_command()

    assert controller.robot.report_position() == "Robot Not Yet Placed"     # Robot should not have been placed

