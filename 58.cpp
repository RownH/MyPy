class Solution {
public:
	string reverseWords(string s) {
		int i, j;
		i = j = s.length() - 1;
		if (i < 0) {
			return s;
		}
		string res = "";
		while (i >= 0) {
			while (i >= 0 && s[i] != ' ') {
				--i;
			}
			string temp = s.substr(i + 1, j - i);
			while (i >= 0 && s[i] == ' ') {
				--i;
			}
			if (s[j] != ' ') {
				if (i > -1) {
					res += temp + " ";
				}
				else {
					res += temp;
				}
			}
			j = i;
		}
		return res;

	}
};