import pytest
from textual.pilot import Pilot
from src.interfaces.tui.app import TodoApp

@pytest.fixture
def pilot():
    app = TodoApp()
    return Pilot(app)

async def test_initial_screen(pilot: Pilot):
    await pilot.press("a")
    await pilot.pause()
    assert pilot.app.query_one("#title").placeholder == "Title"
    await pilot.press("escape")

async def test_add_task(pilot: Pilot):
    await pilot.press("a")
    await pilot.pause()
    await pilot.type("Test Task")
    await pilot.press("tab")
    await pilot.type("Test Description")
    await pilot.press("enter")
    await pilot.pause()
    assert "Test Task" in pilot.app.query_one("TaskList")._data[1][1]
