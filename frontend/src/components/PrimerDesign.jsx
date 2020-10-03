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

class PrimerDesign extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            dnaRegion: '',
            primerLength: '',
            proteinSequence: null,
            resultsError: null,
        };
    }

    handleTextBoxChange = (event) => {
        this.setState({
            dnaRegion: event.target.value.toUpperCase(),
            primerLength: event.target.value,
            proteinSequence: null,
            resultsError: null,
        });
    };

    submit = () => {
        axios
            .post('/api/primer', {
                dna_region: this.state.dnaRegion,
                primer_length: this.state.primerLength,
            })
            .then((res) => {
                this.setState({ genPrimes: res.data });
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
        if (this.state.genPrimes === null) {
            return <div></div>;
        }
        return (
            <div>
                <Typography className={classes.resultsTitle}>
                    Primers for this region
                </Typography>
                <div className={classes.resultsContainer}>
                    {this.state.genPrimes}
                </div>
            </div>
        );
    };

    render() {
        const { classes } = this.props;
        return (
            <div>
                <Typography variant="h6" className={classes.title}>
                    Design Primer
                </Typography>
                <TextField
                    id="outlined-multiline-static"
                    label="Region to amplify"
                    value={this.state.dnaRegion}
                    variant="outlined"
                    name="dnaRegion"
                    error={this.state.inputError}
                    className={classes.inputTextBox}
                    onChange={this.handleTextBoxChange}
                />
                <TextField
                    id="outlined-multiline-static"
                    label="Primer length"
                    value={this.state.primerLength}
                    variant="outlined"
                    name="primerLength"
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

PrimerDesign.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(PrimerDesign);
