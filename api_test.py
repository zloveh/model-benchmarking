from evalscope.perf.main import run_perf_benchmark
from customApi.custom import CustomZhuquePlugin

task_cfg = {"url": "https://test-api.xxx.com/api/v1/stream",
            "parallel": 2,
            "model": "test2.5",
            "number": 4,
            "api": "customZhuque",
            "dataset": "openqa",
            "dataset_path": "./customDataset/dataset_infos.jsonl",
            "stream": True,
            "query_template": '{"conversationId":"","userMsg":""}',
            }
run_perf_benchmark(task_cfg)