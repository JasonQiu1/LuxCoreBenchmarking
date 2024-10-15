#/bin/bash
suffix=""
if [ "$#" -eq 1 ]; then
    suffix="_$1"
fi

sftp memorylab << EOF
get /home/jq48/LinuxCompile/target-64-sse2/LuxCoresdk/benchmark.png
EOF

mv benchmark.png "benchmark$suffix.png"
