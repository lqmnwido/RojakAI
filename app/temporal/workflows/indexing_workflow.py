from datetime import timedelta

from temporalio import workflow

@workflow.defn
class IndexingWorkflow:
    @workflow.run
    async def run(self, path: str) -> str:
        return await workflow.execute_activity(
            "run",
            path,
            start_to_close_timeout=timedelta(minutes=30),
        )