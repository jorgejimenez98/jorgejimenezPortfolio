import emoji from "react-easy-emoji";

export const portfolioEn = {
  cv_links: {
    simple:
      "https://drive.google.com/file/d/1vGt9SvVAOv-2HceBGfNIs90MCgnDGbrr/view?usp=sharing",
    modern:
      "https://drive.google.com/file/d/1Q3--4nlcPTrohhNaGjTem5lhw-kXYE7g/view?usp=sharing",
  },
  labels: {
    contact: "Contact Me",
    send_email_direct: "Send email directly",
    go_back: "Go Back",
    spain: "Spain",
    experience: "Work Experience",
    madeBy: emoji("Made with ❤️ by Jorge Jiménez"),
    check: "Check code",
    here: "here",
    open: "Open to Work",
    currentlyWorking: "Currenctly Working",
    tech: "Technologies",
    present: "Present",
    keyExperience: "Key Experience",
    cv_button: "See my CV",
    modal_title: "Download CV in English.",
    simple_design: "CV simple Design",
    simple_modern: "CV modern Design",
    change_lang_dialog:
      "If you want to consult the CV in another language, simply change it from the header",
  },
  conctactForm: {
    nameLabel: "Full Name",
    namePlaceHolder: "Write here your name",
    emailLabel: "Email",
    emailPlaceHolder: "Write here your email",
    messageLabel: "Message",
    messagePlaceHolder: "Write here the message",
    send: "Send",
    sended: "Email Sended successfully",
    validations: {
      emailRequired: "Email is required",
      validEmail: "Write a valid email. Example: name@gmail.com",
      nameRequired: "Full name is required",
      messRequired: "Message is required",
    },
  },
  contactInfo: {
    title: emoji("Contact Me ☎️"),
    subtitle:
      "Discuss a project or just want to say hi? My Inbox is open for all.",
  },
  techStack: {
    favorite: "My main technologies",
    tools: "Technologies",
    experience: [
      {
        Stack: "Backend with Django",
        progressPercentage: "98%",
      },
      {
        Stack: "Build APIS with django-rest-framework",
        progressPercentage: "95%",
      },
      {
        Stack: "Frontend with React",
        progressPercentage: "90%",
      },
    ],
  },
};
