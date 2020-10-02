import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios';

const styles = (theme) => ({
    submitButton: {
        marginLeft: theme.spacing(2),
        marginTop: theme.spacing(1),
    },
    title: {
        marginBottom: theme.spacing(2),
    },
    resultsTitle: {
        fontWeight: 'bold',
        marginTop: theme.spacing(2),
    },
    resultsContainer: {
        marginTop: theme.spacing(1),
    },
});

class DNATranslator extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            dnaSequence: '',
            proteinSequence: null,
            resultsError: null,
        };
    }

    handleTextBoxChange = (event) => {
        this.setState({
            dnaSequence: event.target.value.toUpperCase(),
            proteinSequence: null,
            resultsError: null,
        });
    };

    submit = () => {
        axios
            .post('/api/translate', { dna_sequence: this.state.dnaSequence })
            .then((res) => {
                this.setState({ proteinSequence: res.data });
            })
            .catch((err) => {
                this.setState({ resultsError: err.response.data.detail });
            });
    };

    renderResults = (classes) => {
        if (this.state.resultsError) {
            return (
                <div>
                    <Typography className={classes.resultsTitle}>
                        Error
                    </Typography>
                    <div className={classes.resultsContainer}>
                        {this.state.resultsError}
                    </div>
                </div>
            );
        }
        if (this.state.proteinSequence === null) {
            return <div></div>;
        }
        return (
            <div>
                <Typography className={classes.resultsTitle}>
                    Protein Sequence
                </Typography>
                <div className={classes.resultsContainer}>
                    {this.state.proteinSequence}
                </div>
            </div>
        );
    };

    render() {
        const { classes } = this.props;
        return (
            <div>
                <Typography variant="h6" className={classes.title}>
                    Translate a DNA sequence
                </Typography>
                <TextField
                    id="outlined-multiline-static"
                    label="DNA Sequence"
                    value={this.state.dnaSequence}
                    variant="outlined"
                    name="dnaSequence"
                    error={this.state.inputError}
                    className={classes.inputTextBox}
                    onChange={this.handleTextBoxChange}
                />
                <Button
                    variant="contained"
                    color="primary"
                    onClick={this.submit}
                    className={classes.submitButton}
                >
                    Submit
                </Button>
                <div>{this.renderResults(classes)}</div>
            </div>
        );
    }
}

DNATranslator.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(DNATranslator);
