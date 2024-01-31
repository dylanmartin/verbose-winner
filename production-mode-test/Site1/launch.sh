docker run --rm --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name site1 \
    -v /$(pwd)/to_mount:/workspace/ \
    nvflare-pt:latest \
    //bin/bash -c "provisioned/startup/start.sh; tail -f /dev/null"