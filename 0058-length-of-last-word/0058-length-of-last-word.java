class Solution {
    public int lengthOfLastWord(String s) {
        String words[]=s.split(" ");
        String lastworld=words[words.length-1];
        int length=lastworld.length();
        return length;

    }
}