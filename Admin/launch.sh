docker run --rm --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name Admin \
    -v /$(pwd)/to_mount:/workspace/ \
    nvflare-pt:latest \
    //bin/bash -c "python admin.py; tail -f /dev/null"