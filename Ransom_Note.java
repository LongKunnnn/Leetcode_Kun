class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] counts = new int[26];
        for (char c : magazine.toCharArray()) {
            counts[c - 'a']++;
        }

        for (char c : ransomNote.toCharArray()) {
            int idx = c - 'a';
            if (counts[idx] == 0) {
                return false;
            } 
            counts[idx]--;
            
        }
        return true;
    }
}