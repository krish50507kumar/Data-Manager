
import pytest
from unittest.mock import Mock

from data_manager.runner import Runner


def test_run_with_no_works():
    runner = Runner([])

    result = runner.run()

    assert result is None


def test_run_single_job():
    job = Mock()

    works = [
        {
            "job": job,
            "contexts": [{"task": "removeNull"}]
        }
    ]

    runner = Runner(works)

    runner.run()

    job.run.assert_called_once_with(
        [{"task": "removeNull"}]
    )


def test_run_multiple_jobs():
    job1 = Mock()
    job2 = Mock()

    works = [
        {
            "job": job1,
            "contexts": [{"task": "job1"}]
        },
        {
            "job": job2,
            "contexts": [{"task": "job2"}]
        }
    ]

    runner = Runner(works)

    runner.run()

    job1.run.assert_called_once_with(
        [{"task": "job1"}]
    )

    job2.run.assert_called_once_with(
        [{"task": "job2"}]
    )


def test_exception_is_propagated():
    job = Mock()
    job.run.side_effect = RuntimeError("boom")

    works = [
        {
            "job": job,
            "contexts": []
        }
    ]

    runner = Runner(works)

    with pytest.raises(RuntimeError, match="boom"):
        runner.run()

def test_jobs_run_in_order():
    execution_order = []

    class Job:
        def __init__(self, name):
            self.name = name

        def run(self, context):
            execution_order.append(self.name)

    works = [
        {"job": Job("engineer"), "contexts": []},
        {"job": Job("analytics"), "contexts": []},
        {"job": Job("graph"), "contexts": []},
    ]

    Runner(works).run()

    assert execution_order == [
        "engineer",
        "analytics",
        "graph",
    ]