docker run --rm --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name server2 \
    -p 8102:8102 -p 8103:8103 \
    -v //c/development/verbose-winner/my-workspace/workspace/example_project/prod_00/server2:/provision \
    -w //my-workspace \
    nvflare-pt:latest \
    //bin/bash -c "../provision/startup/start.sh; tail -f /dev/null"