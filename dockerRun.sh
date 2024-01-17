docker run --rm -it --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    --name flare \
    -v /$(pwd)/my-workspace:/my-workspace \
    -w //my-workspace \
    nvflare-pt:latest