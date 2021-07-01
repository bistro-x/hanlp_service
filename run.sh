if [ ! -d "./log/" ];then
  mkdir ./log
fi

time_out=${TIME_OUT:-600}
param_str=${PARAM_STR}

echo "time_out:$time_out"
echo "param_str:$param_str"

gunicorn -w 1 -t $time_out  --worker-connections 2000  $param_str -b 0.0.0.0:5000 run:app
