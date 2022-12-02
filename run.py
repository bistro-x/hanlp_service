# -*- coding: utf-8 -*-

import hanlp
import os
from flask import request, jsonify, Flask

hanlp_engine = hanlp.load(
    hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH
)

app = Flask(__name__, root_path=os.getcwd())


@app.route("/participle", methods=["POST"])
def participle():
    """
    分词
    """

    param = {**(request.form or {}), **(request.json or {})}
    sentence = param.get("sentence", "")

    result = hanlp_engine(sentence, tasks="tok/fine").get("tok/fine")

    return jsonify({"result": result})


@app.route("/lexical", methods=["POST"])
def lexical():
    """分词解析

    Returns:
        _type_: _description_
    """
    param = {**(request.form or {}), **(request.json or {})}
    sentence = param.get("sentence", "")

    result = hanlp_engine(sentence, tasks="pos/pku").get("pos/pku")

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
