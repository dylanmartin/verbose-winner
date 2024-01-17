docker run --rm --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name host.docker.internal \
    -p 8002:8002 -p 8003:8003 \
    -v //c/development/verbose-winner/my-workspace/workspace/example_project/prod_00/host.docker.internal:/provision \
    -w //my-workspace \
    nvflare-pt:latest \
    //bin/bash -c "../provision/startup/start.sh; tail -f /dev/null"