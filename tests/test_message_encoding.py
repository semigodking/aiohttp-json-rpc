from datetime import datetime

import pytest

from aiohttp_json_rpc.protocol import encode_request


@pytest.mark.skipif(pytest.importorskip('pandas') is None,
                    reason='No pandas support')
def test_datetime_serialization():
    encode_request('abc', params={'p': datetime.now()})
