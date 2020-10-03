import React from 'react';
import PropTypes from 'prop-types';

import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Typography from '@material-ui/core/Typography';
import Toolbar from '@material-ui/core/Toolbar';

import DNATranslator from '../components/DNATranslator';
import PrimerDesign from '../components/PrimerDesign';

const styles = (theme) => ({
    root: {
        zIndex: theme.zIndex.drawer + 1,
        position: 'fixed',
        width: '100%',
    },
    brandmarkContainer: {
        width: '30px',
        height: '30px',
        display: 'flex',
        justifyContent: 'center',
        marginRight: theme.spacing(1),
    },
    inlineBottom: {
        display: 'flex',
        alignItems: 'baseline',
    },
    toolsContainer: {
        marginLeft: theme.spacing(4),
        marginTop: theme.spacing(4),
    },
});

function Root(props) {
    const { classes } = props;

    return (
        <div className={classes.root}>
            <AppBar position="static" color="default">
                <Toolbar>
                    <div className={classes.brandmarkContainer}>
                        <img width={60} src="/assets/brandmark.svg" />
                    </div>
                    <div className={classes.inlineBottom}>
                        <Typography variant="h6" color="inherit">
                            Design Tools
                        </Typography>
                    </div>
                </Toolbar>
            </AppBar>
            <div className={classes.toolsContainer}>
                <DNATranslator />
                <PrimerDesign />
            </div>
        </div>
    );
}

Root.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Root);
