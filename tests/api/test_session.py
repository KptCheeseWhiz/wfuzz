import pytest
import wfuzz


@pytest.mark.parametrize(
    "session, expected_result",
    [
        (
            '-z range,0-4 http://127.0.0.1/FUZZ',
            {
                'allvars': None,
                'auth': (None, None),
                'colour': False,
                'compiled_baseline': None,
                'compiled_dictio': None,
                'compiled_filter': None,
                'compiled_prefilter': [],
                'compiled_printer': None,
                'compiled_seed': None,
                'compiled_stats': None,
                'concurrent': 10,
                'conn_delay': 90,
                'connect_to_ip': None,
                'console_printer': '',
                'cookie': [],
                'delay': None,
                'dictio': None,
                'exec_mode': 'api',
                'fields': [],
                'filter': '',
                'follow': False,
                'hc': [],
                'headers': [],
                'hh': [],
                'hl': [],
                'hs': None,
                'hw': [],
                'interactive': False,
                'iterator': None,
                'method': None,
                'no_cache': False,
                'payloads': [('range', {'default': '0-4', 'encoder': None}, None)],
                'postdata': None,
                'prefilter': [],
                'previous': False,
                'printer': (None, None),
                'proxies': None,
                'recipe': [],
                'req_delay': 90,
                'retries': 3,
                'rlevel': 0,
                'save': '',
                'sc': [],
                'scanmode': False,
                'script': '',
                'script_args': {},
                'seed_payload': False,
                'sh': [],
                'show_field': None,
                'sl': [],
                'ss': None,
                'sw': [],
                'transport': 'http',
                'url': 'http://127.0.0.1/FUZZ',
                'verbose': False,
            }
        )
    ]
)
def test_get_payload(session, expected_result):
    assert wfuzz.get_session(session).data == expected_result
