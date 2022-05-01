const getTextTranslated = (arrayList, language) => {
  return arrayList.find((item) => item?.language === language)?.text;
};

export default getTextTranslated;
