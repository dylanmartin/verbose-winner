docker run --rm --gpus all \
    --name overseer \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    -p 8443:8443 \
    -v //c/development/verbose-winner/my-workspace/workspace/example_project/prod_00/overseer:/provision \
    -w //my-workspace \
    nvflare-pt:latest \
    //bin/bash -c "../provision/startup/start.sh; tail -f /dev/null"