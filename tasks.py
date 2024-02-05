from invoke import task

@task
def watch(c):
    c.run("nodemon --exec python3 ./src/example.py")