import React from "react";

function InputFullName({ portfolio, formik }) {
  return (
    <div className="form-group">
      {/* FULL NAME */}
      <label>{portfolio.conctactForm.nameLabel}</label>
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
        placeholder={portfolio.conctactForm.namePlaceHolder}
      />
      {formik.touched.fullName && Boolean(formik.errors.fullName) && (
        <small className="error-text">{formik.errors.fullName}</small>
      )}
    </div>
  );
}

export default InputFullName;
