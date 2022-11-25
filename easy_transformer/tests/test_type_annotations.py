from typeguard.importhook import install_import_hook

install_import_hook("easy_transformer")

from torchtyping import TensorType as TT
from torchtyping import patch_typeguard

from easy_transformer import EasyTransformer

patch_typeguard()

# n.b. that i used this file to see if my type annotations were working- they were! i occasionally
# changed one of the sizes and saw that the type checker caught it.


def test_type_annotations():
    MODEL = "gpt2"
    model = EasyTransformer.from_pretrained(MODEL)

    prompt = "Hello World!"
    tokens = model.to_tokens(prompt, prepend_bos=False)
    logits_tokens = model(tokens)
    logits_text: TT[1, "n_tokens", "d_vocab"] = model(prompt, prepend_bos=False)
