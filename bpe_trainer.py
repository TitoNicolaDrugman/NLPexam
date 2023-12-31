import re
import collections
from typing import Union

import utils
import collections


class BPE(object):
    def __init__(
        self, 
        vocab: Union[str, dict], 
        end_token: str = '</w>', 
        unknown_token: str = "<UNK>"
    ) -> None:
        super().__init__()
        if isinstance(vocab, str):
            self.vocab = utils.create_vocab_from_file(vocab)
        elif isinstance(vocab, dict):
            self.vocab = vocab
        else:
            raise TypeError(
                "vocab must be either str (text file path) or dict (vocab)"
            )

        self.end_token = end_token
        self.unknown_token = unknown_token
        self.tokens = None
        self.words_to_tokens = None

    def train(self, iterations: int) -> None:
        if not isinstance(iterations, int):
            raise TypeError("iterations must be int")

        for i in range(iterations):
            token_pairs = self.__get_pairs()

            # stop if there are no more pairs
            if not token_pairs:
                break

            # get the most frequent pair, merge those, create new tokens
            # and update the vocab
            most_frequent_pair = max(token_pairs, key=token_pairs.get)
            self.__merge_tokens_and_update_vocab(most_frequent_pair)

        # finally, get the tokens and frequencies
        tokens, words_to_tokens = utils.get_tokens_from_vocab(self.vocab)
        self.tokens = self.__sort_tokens(tokens)
        self.words_to_tokens = words_to_tokens

        print("Training finished")

    def tokenize(self, word, tokens=None) -> list:
        word += self.end_token
        return self.__tokenize(word, tokens)

    def __tokenize(self, word: str, tokens: list = None) -> list:
        if tokens is None:
            tokens = self.tokens

        if word in self.words_to_tokens:
            return self.words_to_tokens[word]
        if word == "":
            return []
        if tokens == []:
            return [self.unknown_token]

        out_tokens = []
        for i in range(len(self.tokens)):
            temp_token = self.tokens[i]
            esc_token = re.escape(temp_token.replace('.', '[.]'))

            matched_indices = [(matched.start(0), matched.end(0))
                               for matched in re.finditer(esc_token, word)]
            if len(matched_indices) == 0:
                continue

            subword_end_indices = [matched_index[0]
                                   for matched_index in matched_indices]
            subword_start_index = 0

            for end_index in subword_end_indices:
                subword = word[subword_start_index:end_index]
                out_tokens.extend(self.__tokenize(subword, self.tokens[i + 1:]))
                out_tokens.append(temp_token)
                subword_start_index = end_index + len(temp_token)

            remaining_subword = word[subword_start_index:]
            out_tokens.extend(self.__tokenize(remaining_subword, self.tokens[i + 1:]))
            break
        return out_tokens

    def __get_pairs(self):
        pairs = collections.defaultdict(int)

        for tokens, count in self.vocab.items():
            chars = tokens.split()

            for i in range(len(chars) - 1):
                pairs[(chars[i], chars[i + 1])] += count

        return pairs

    def __merge_tokens_and_update_vocab(self, pair):
        temp_vocab = {}

        pattern = re.compile(
            r'(?<!\S)' + re.escape(' '.join(pair)) + r'(?!\S)')
        for token in self.vocab:
            updated_token = pattern.sub(''.join(pair), token)
            temp_vocab[updated_token] = self.vocab[token]

        self.vocab = temp_vocab

    def __sort_tokens(self, tokens_with_freq: dict) -> list:
        if not isinstance(tokens_with_freq, dict):
            raise TypeError("`tokens_with_freq` must be a `dict`")

        sorted_tokens = sorted(tokens_with_freq.items(),
                               key=lambda x: (len(x[0]), x[1]), reverse=True)
        sorted_tokens = [token for token, _ in sorted_tokens]

        return sorted_tokens
