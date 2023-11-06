import java.util.ArrayList;
import java.util.List;

class Solution1592 {
    public String reorderSpaces(String text) {
        int wordLength = 0;
        String[] wordArray = text.split(" ");
        List<String> words = new ArrayList<>(wordArray.length);
        for (String word : wordArray) {
            if (!word.isEmpty()) {
                words.add(word);
                wordLength += word.length();
            }
        }
        int extraSpace;
        StringBuilder end = new StringBuilder();
        if (words.size() == 1) {
            extraSpace = text.length() - wordLength;
            for (int i = 0; i < extraSpace; i++) {
                end.append(" ");
            }
            return words.get(0) + end;
        } else {
            int spacesNum = (text.length() - wordLength) / (words.size() - 1);
            extraSpace = text.length() - wordLength - spacesNum * (words.size() - 1);
            StringBuilder sequence = new StringBuilder();
            for (int i = 0; i < spacesNum; i++) {
                sequence.append(" ");
            }
            for (int i = 0; i < extraSpace; i++) {
                end.append(" ");
            }
            return String.join(sequence.toString(), words) + end;
        }
    }
}