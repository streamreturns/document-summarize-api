from ROUGEMetrics import ROUGEMetrics


class ROUGESummarization:
    def __init__(self, rouge_metric='ROUGE1-F1'):
        assert rouge_metric.upper() == 'ROUGE1-F1', 'currently only supports ROUGE1-F1 summarization'
        self.rouge_metrics = ROUGEMetrics(metrics=['rouge-n'], max_n=1)

        def summarize(sentences, top_n_sentences):
            f1_scores_by_index = dict()
            for i in range(len(sentences)):
                hypothesis = sentences.pop(0)
                reference = ' '.join(sentences)

                rouge1_f1 = self.rouge_metrics.get_scores(hypothesis, reference)['rouge-1']['f']
                f1_scores_by_index[i] = rouge1_f1
                #print(rouge1_f1, hypothesis)

                sentences.append(hypothesis)

            summarization = list()
            for i, f1_score in sorted(f1_scores_by_index.items(), key=lambda item: item[1], reverse=True):
                if len(summarization) <= top_n_sentences:
                    if len(sentences[i]) > 1:
                        summarization.append(sentences[i])
                    # print('%.5f' % f1_score, sentences[i])

            return summarization