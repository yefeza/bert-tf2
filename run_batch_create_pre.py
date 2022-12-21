import subprocess

start_corpus = 142
end_corpus = 203
for i in range(start_corpus, end_corpus):
    print("Creating corpus " + str(i))
    subprocess.call(["python", "create_pretraining_data.py", "--input_file=gs://squad-juristeca/inputs/corpus/corpus.txt_" + str(i), "--output_file=gs://squad-juristeca/inputs/tf_records/scratch_version_2/tf_examples.tfrecord_0000" + str(i), "--vocab_file=gs://squad-juristeca/scratch_version_2/vocab.txt", "--do_lower_case=False", "--max_seq_length=128", "--max_predictions_per_seq=20", "--masked_lm_prob=0.15", "--random_seed=56489", "--dupe_factor=2"])
