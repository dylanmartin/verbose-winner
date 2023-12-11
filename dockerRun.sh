docker run --rm -it --gpus all \
    --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
    -v /$(pwd)/my-workspace:/my-workspace \
    -w //my-workspace \
    nvflare-pt:latest