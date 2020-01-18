from course.models import CognitiveLevel, ActionVerb
import csv


def import_data_from_csv():
    with open("Data/CSV/ActionVerbsBloomTaxonomy.csv", "r") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        action_verb_list = []
        cognitive_level_list = []
        for row in readCSV:
            action_verb_list.append(row[0])
            cognitive_level_list.append(row[1])

        for cognitive_level in set(cognitive_level_list):
            if not CognitiveLevel.objects.filter(
                cognitive_level=cognitive_level
            ):
                CognitiveLevel.objects.create(cognitive_level=cognitive_level)

        for i, action_verb in enumerate(action_verb_list):
            if not ActionVerb.objects.filter(action_verb=action_verb):
                cognitive_level = CognitiveLevel.objects.get(
                    cognitive_level=cognitive_level_list[i]
                )
                ActionVerb.objects.create(
                    action_verb=action_verb, cognitive_level=cognitive_level
                )
