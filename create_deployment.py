from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/RichardMan13/prefect_demo.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="prefect_demo.py:repo_info", # Specific flow to run
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool", # Work pool target
        cron="0 1 * * *", # Cron schedule (1am every day)
    )


