import * as yup from "yup";

export const initialValues = {
  fullName: "",
  email: "",
  message: "",
};

export const validationSchema = yup.object({
  fullName: yup.string().trim().required("Full name is required"),
  email: yup
    .string()
    .email("Write a valid email. Example: name@email.com")
    .required("Email is required"),
  message: yup.string().trim().required("Message is required"),
});
