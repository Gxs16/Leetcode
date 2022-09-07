class Solution {
    public String reorderSpaces(String text) {
        int wordLength = 0;
        String[] wordArray = text.split(" ");
        List<String> words = new ArrayList<>(wordArray.length);
        for (String word: wordArray) {
            if (word.length()>0) {
                words.add(word);
                wordLength += word.length();
            }
        }
        int extraSpace = 0;
        String end = "";
        if (words.size() == 1) {
            extraSpace = text.length()-wordLength;
            for (int i = 0; i < extraSpace; i++) {
                end += " ";
            }
            return words.get(0)+end;
        } else {
            int spacesNum = (text.length()-wordLength)/(words.size()-1);
            extraSpace = text.length()-wordLength-spacesNum*(words.size()-1);
            String sequence = "";
            for (int i = 0; i < spacesNum; i++) {
                sequence += " ";
            }
            for (int i = 0; i < extraSpace; i++) {
                end += " ";
            }
            return String.join(sequence, words)+end;
        }
    }
}