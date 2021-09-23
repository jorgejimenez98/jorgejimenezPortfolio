import React from "react";
import { useFormik } from "formik";
import Button from "@mui/material/Button";
import SendIcon from "@material-ui/icons/Send";
import { initialValues, validationSchema } from "./contact_validation";

function ContactForm() {
  const formik = useFormik({
    initialValues: initialValues,
    validationSchema: validationSchema,
    validateOnChange: true,
    validateOnBlur: true,
    onSubmit: (values) => {
      const templateId = "template_iwap21m";
      const serviceId = "service_qexph0s";
      window.emailjs
        .send(serviceId, templateId, {
          reply_to: values.email,
          fullName: values.fullName,
          message: values.message,
        })
        .then((res) => {
          alert("Email successfully sent!");
        })
        // Handle errors here however you like, or use a React error boundary
        .catch((err) =>
          console.log(
            "Oh well, you failed. Here some thoughts on the error that occured:",
            err
          )
        );
    },
  });

  return (
    <div className="container mt-4">
      <form onSubmit={formik.handleSubmit}>
        <div className="form-group">
          {/* FULL NAME */}
          <label>Full Name</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            onChange={formik.handleChange}
            className={
              formik.touched.fullName && Boolean(formik.errors.fullName)
                ? "form-control is-invalid"
                : formik.touched.fullName && !Boolean(formik.errors.fullName)
                ? "form-control is-valid"
                : "form-control"
            }
            value={formik.values.fullName}
            placeholder="Write here your name"
          />
          {formik.touched.fullName && Boolean(formik.errors.fullName) && (
            <small className="error-text">{formik.errors.fullName}</small>
          )}
        </div>

        {/* EMAIL */}
        <div className="form-group mt-4">
          <label>Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formik.values.email}
            onChange={formik.handleChange}
            className={
              formik.touched.email && Boolean(formik.errors.email)
                ? "form-control is-invalid"
                : formik.touched.email && !Boolean(formik.errors.email)
                ? "form-control is-valid"
                : "form-control"
            }
            placeholder="Write here your email"
          />
          {formik.touched.email && Boolean(formik.errors.email) && (
            <small className="error-text">{formik.errors.email}</small>
          )}
        </div>

        {/* MESSAGE */}
        <div className="form-group mt-4">
          <label>Message</label>
          <textarea
            rows="5"
            id="message"
            name="message"
            className={
              formik.touched.message && Boolean(formik.errors.message)
                ? "form-control is-invalid"
                : formik.touched.message && !Boolean(formik.errors.message)
                ? "form-control is-valid"
                : "form-control"
            }
            value={formik.values.message}
            onChange={formik.handleChange}
            placeholder={"Write here the message"}
          ></textarea>
          {formik.touched.message && Boolean(formik.errors.message) && (
            <small className="error-text">{formik.errors.message}</small>
          )}
        </div>

        <Button
          variant="contained"
          type="submit"
          disabled={!formik.isValid}
          endIcon={<SendIcon />}
        >
          Send
        </Button>
      </form>
    </div>
  );
}

export default ContactForm;
