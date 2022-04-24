import React, { useEffect } from "react";
import { useFormik } from "formik";
// Redux Imports
import { useSelector, useDispatch } from "react-redux";
import { send_email } from "../redux/actions/emailActions";
import { setSnackbar } from "../redux/actions/snackBarActions";
import { EMAIL } from "../redux/constants/emailConstants";
// Components
import Loader from "../containers/Loader";
import Button from "@mui/material/Button";
import SendIcon from "@material-ui/icons/Send";
import InputFullName from "./Inputs/InputFullName";
import InputEmail from "./Inputs/InputEmail";
import InputMessage from "./Inputs/InputMessage";
import * as yup from "yup";

function ContactForm() {
  const dispatch = useDispatch();
  const { portfolio, languaje } = useSelector((state) => state.languaje);

  const {
    loading: loadingSend,
    success: successSend,
    error: errorSend,
  } = useSelector((state) => state.emailSend);

  const initialValues = {
    fullName: "",
    email: "",
    message: "",
  };

  const validationSchema = yup.object({
    fullName: yup
      .string()
      .trim()
      .required(portfolio.conctactForm.validations.nameRequired),
    email: yup
      .string()
      .email(portfolio.conctactForm.validations.validEmail)
      .required(portfolio.conctactForm.validations.emailRequired),
    message: yup
      .string()
      .trim()
      .required(portfolio.conctactForm.validations.messRequired),
  });

  const formik = useFormik({
    initialValues: initialValues,
    validationSchema: validationSchema,
    validateOnChange: true,
    validateOnBlur: true,
    onSubmit: (values) => {
      const params = {...values, languaje}
      dispatch(send_email(params));
    },
  });

  useEffect(() => {
    if (successSend) {
      const message = portfolio.conctactForm.sended;
      dispatch(setSnackbar(true, "success", message));
      formik.resetForm();
    }
    if (errorSend) {
      dispatch(setSnackbar(true, "error", errorSend));
    }
    return () => {
      dispatch({ type: EMAIL.RESET });
    };
    // eslint-disable-next-line
  }, [successSend, errorSend, dispatch, portfolio]);

  return (
    <div className="container mt-4">
      <form onSubmit={formik.handleSubmit}>
        <InputFullName portfolio={portfolio} formik={formik} />
        <InputEmail portfolio={portfolio} formik={formik} />
        <InputMessage portfolio={portfolio} formik={formik} />

        {loadingSend && <Loader />}

        <div className="text-center mt-3">
          <Button
            variant="contained"
            type="submit"
            disabled={!formik.isValid}
            endIcon={<SendIcon />}
          >
            {portfolio.conctactForm.send}
          </Button>
        </div>
      </form>
    </div>
  );
}

export default ContactForm;
