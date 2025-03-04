/**
 * @param {string} s
 * @return {string}
 */

/**
 * take: to have a hashmap of all the char positions and loop through s again and string slice
 */
var longestPalindrome = function (s) {
  const hm = {};
  for (let i = 0; i < s.length; i++) {
    if (!hm[s[i]]) {
      hm[s[i]] = [i];
    } else {
      hm[s[i]].push(i);
    }
  }
  for (key of Object.keys(hm)) {
    if (hm[key].length == 1) {
      delete hm[key];
    }
  }
  let longest = "";
  // need to use the position so keep i
  for (let i = 0; i < s.length; i++) {
    if (!hm[s[i]]) {
      continue;
    }
    for (let pos of hm[s[i]]) {
      // get the substr
      if (i >= pos) {
        let possible = s.substr(pos, i + 1 - pos);
        let reverse = s
          .substr(pos, i + 1 - pos)
          .split("")
          .reverse()
          .join("");
        // console.log(`pos: ${possible} rev: ${reverse} cut: ${pos} #${pos - i}`);
        if (possible == reverse) {
          if (possible.length > longest.length) {
            longest = possible;
            break;
          }
        }
      }
    }
  }
  return longest;
};

console.log(
  longestPalindrome(
    "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftvhpdgjjfafunfndztdjkcxyihtsyppendfzzjeyxlbwpdygiqmdqcdbmgyjigrmfkswcwryaydjilqqxvcnyvviesuncslvzikawwqykqwdfibggezufqihcjkebapmgkvwixywgdextafxycnipjglsndkyjoqfyfljfkkvoieksmavdlmlhhnstesibffiopqvlyuidvrawndbzonwzbsjmpeqoglmdbinkovqpzfkxihzitdopnomseqhmrrkcsvrzziphwpuhjngeotwcrebcmbtirkgeavojtmpakcewmexhxacngknokxsvtqobdgckutpexswgwqzbosjpxauyflnylfcxsucsehqvakbpvfmkelmkspsqxnutwfwacpqqvovdqafeylobneojdsgqowcbxfsvuqusdbylcgcvgrofgvzubakjmlbffjhrafvnqttwuyhokzpmhlludpbowuxzrebxsdusalljfjgjkucwzpmndqncykvfnbrxcrcaxwisjpstejjqbpwegpxyrtyafxklgralnkwxkmjpuqfixzkonznmguyizlancpxdzcfkgiotyelegprbaytdhbutbuihkxnbtuqrtezaskfqsmrznfohhlqp",
  ),
);
