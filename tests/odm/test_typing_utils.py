from typing import Optional, Union

from beanie.odm.utils.typing import extract_id_class


class TestTyping:
    def test_extract_id_class(self):
        # Union
        assert extract_id_class(Union[str, int]) == str
        assert extract_id_class(Union[str, None]) == str
        assert extract_id_class(Union[str, None, int]) == str
        # Optional
        assert extract_id_class(Optional[str]) == str
