import React from "react";

function InputEmail({ portfolio, formik }) {
  return (
    <div className="form-group mt-4">
      {/* EMAIL */}
      <label>{portfolio.conctactForm.emailLabel}</label>
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
        placeholder={portfolio.conctactForm.emailPlaceHolder}
      />
      {formik.touched.email && Boolean(formik.errors.email) && (
        <small className="error-text">{formik.errors.email}</small>
      )}
    </div>
  );
}

export default InputEmail;
