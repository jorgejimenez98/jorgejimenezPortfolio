import React from "react";

function InputMessage({ portfolio, formik }) {
  return (
    <div className="form-group mt-4">
      {/* MESSAGE */}
      <label>{portfolio.conctactForm.messageLabel}</label>
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
        placeholder={portfolio.conctactForm.messagePlaceHolder}
      ></textarea>
      {formik.touched.message && Boolean(formik.errors.message) && (
        <small className="error-text">{formik.errors.message}</small>
      )}
    </div>
  );
}

export default InputMessage;
