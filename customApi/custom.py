import json
from typing import Any, Dict, Iterator, List

from evalscope.perf.arguments import Arguments
from evalscope.perf.plugin.api.base import ApiPluginBase
from evalscope.perf.plugin.registry import register_api
from evalscope.utils.logger import get_logger

logger = get_logger()


@register_api('customZhuque')
class CustomZhuquePlugin(ApiPluginBase):
    """Support tensorrt-llm triton server
    """

    def __init__(self, mode_path: str):
        """Init the plugin

        Args:
            mode_path (str): The model path, we use the tokenizer
                weight in the model to calculate the number of the
                input and output tokens.
        """
        super().__init__(model_path=mode_path)
        if mode_path is not None:
            from modelscope import AutoTokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(mode_path)
        else:
            self.tokenizer = None

    def build_request(self, messages: List[Dict], param: Arguments) -> Dict:
        """Build the openai format request based on prompt, dataset

        Args:
            message (Dict): The basic message to generator query.
            param (Arguments): The query parameters.

        Raises:
            Exception: NotImplemented

        Returns:
            Dict: The request body. None if prompt format is error.
        """
        try:
            query = json.loads(param.query_template)
            query["userMsg"] = messages
            return query
        except Exception as e:
            logger.exception(e)
            logger.error('Prompt: %s invalidate!' % messages)
            return None

    def parse_responses(self, responses, request: Any = None, **kwargs) -> Dict:
        # full_response_content = ''
        # delta_contents = {}
        # input_tokens = None
        # output_tokens = None
        # for response in responses:
        #     data = json.loads(response)
        #     data = data['data']
        #     # {"context_logits":0.0,"cum_log_probs":0.0,"generation_logits":0.0,"model_name":"ensemble",
        #     # "model_version":"1","output_log_probs":[0.0,0.0,0.0,0.0,0.0],"sequence_end":false,"sequence_id":0,"sequence_start":false,"text_output":"性"}
        #     if 'content' in data:
        #         if 0 in delta_contents:
        #             delta_contents[0].append(data['content'])
        #         else:
        #             delta_contents[0] = [data['content']]
        # if input_tokens is None and output_tokens is None and self.tokenizer is not None:
        #     input_tokens = 0
        #     output_tokens = 0
        #     for _, choice_contents in delta_contents.items():
        #         full_response_content = ''.join([m for m in choice_contents])
        #         input_tokens += len(self.tokenizer.encode(request['text_input']))
        #         output_tokens += len(self.tokenizer.encode(full_response_content))
        # elif input_tokens is None and output_tokens is None:  # no usage info get.
        #     input_tokens = 0
        #     output_tokens = 0
        #     logger.warning('No usage info get.')

        return 1, 1 # 忽略token数统计